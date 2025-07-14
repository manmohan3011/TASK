#!/usr/bin/env python3
"""
Final Working Document360 API Script - Fixed Version
"""

import requests
import json
import time

class Document360API:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://apihub.document360.io/v2"
        self.headers = {
            "api_token": api_token,
            "Content-Type": "application/json"
        }
    
    def get_all_folders(self):
        """Get all drive folders"""
        print("Getting all folders...")
        try:
            response = requests.get(f"{self.base_url}/Drive/Folders", headers=self.headers)
            print(f"Response Status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                
                # Handle different response structures
                folders = []
                if isinstance(result, dict):
                    folders = result.get('data', result)
                elif isinstance(result, list):
                    folders = result
                
                print(f"Found {len(folders)} folders")
                for folder in folders:
                    # Handle both 'id' and 'media_folder_id' fields
                    folder_id = folder.get('media_folder_id', folder.get('id', 'No ID'))
                    folder_name = folder.get('media_folder_title', folder.get('title', folder.get('name', 'No name')))
                    print(f"- {folder_name}: {folder_id}")
                return folders
            else:
                print(f"Error: {response.text}")
                return None
        except Exception as e:
            print(f"Error getting folders: {e}")
            return None
    
    def create_folder(self, name, user_id, description="Test folder"):
        """Create a new folder"""
        print(f"Creating folder: {name}")
        
        data = {
            "title": name,
            "description": description,
            "user_id": user_id
        }
        
        try:
            response = requests.post(f"{self.base_url}/Drive/Folders", 
                                   headers=self.headers, 
                                   json=data)
            
            print(f"Response Status: {response.status_code}")
            print(f"Response: {response.text}")
            
            if response.status_code in [200, 201]:
                result = response.json()
                
                # Check if operation was successful
                if result.get('success'):
                    data = result.get('data', {})
                    # Look for media_folder_id first, then id
                    folder_id = data.get('media_folder_id') or data.get('id')
                    
                    if folder_id:
                        print(f"✓ Folder created successfully! ID: {folder_id}")
                        return folder_id
                    else:
                        print("✗ Could not find folder ID in response")
                        print(f"Available keys in data: {list(data.keys())}")
                        return None
                else:
                    print(f"✗ API returned success=false: {result.get('errors', [])}")
                    return None
            else:
                print(f"✗ Failed to create folder: {response.text}")
                return None
                
        except Exception as e:
            print(f"Error creating folder: {e}")
            return None
    
    def update_folder(self, folder_id, new_name, user_id):
        """Update folder name"""
        print(f"Updating folder {folder_id} to: {new_name}")
        
        data = {
            "title": new_name,
        }
        
        try:
            response = requests.put(f"{self.base_url}/Drive/Folders/{folder_id}", 
                                  headers=self.headers, 
                                  json=data)
            
            print(f"Response Status: {response.status_code}")
            print(f"Response: {response.text}")
            
            if response.status_code in [200, 204]:
                print("✓ Folder updated successfully!")
                return True
            elif response.status_code == 200:
                # Check if response has success field
                try:
                    result = response.json()
                    if result.get('success'):
                        print("✓ Folder updated successfully!")
                        return True
                    else:
                        print(f"✗ Update failed: {result.get('errors', [])}")
                        return False
                except:
                    print("✓ Folder updated successfully!")
                    return True
            else:
                print(f"✗ Failed to update folder: {response.text}")
                return False
                
        except Exception as e:
            print(f"Error updating folder: {e}")
            return False
    
    def delete_folder(self, folder_id):
        """Delete a folder"""
        print(f"Deleting folder: {folder_id}")
        
        try:
            response = requests.delete(f"{self.base_url}/Drive/Folders/{folder_id}", 
                                     headers=self.headers)
            
            print(f"Response Status: {response.status_code}")
            print(f"Response: {response.text}")
            
            if response.status_code in [200, 204]:
                print("✓ Folder deleted successfully!")
                return True
            elif response.status_code == 200:
                # Check if response has success field
                try:
                    result = response.json()
                    if result.get('success'):
                        print("✓ Folder deleted successfully!")
                        return True
                    else:
                        print(f"✗ Delete failed: {result.get('errors', [])}")
                        return False
                except:
                    print("✓ Folder deleted successfully!")
                    return True
            else:
                print(f"✗ Failed to delete folder: {response.text}")
                return False
                
        except Exception as e:
            print(f"Error deleting folder: {e}")
            return False

def main():
    # Your credentials
    API_TOKEN = "M1XbCrQnV47mHjZcYnpsUBStnh3QvUqiVv7Jn7oE5VkRiDQmDLbO2eh5LmHqlgsa+zCapZOTjkZyx1Tt6Ym88HmG2+E436HW+jJS28THUUMVb5OQUbps2RRENEybc4K7PtUJz0gOIpqPoBjHlQMenA=="  # Replace with your actual API token
    USER_ID = "b777bb7e-dfa9-4aa8-889a-cbce4e7ef73d"  # Your user ID
    
    if API_TOKEN == "YOUR_API_TOKEN_HERE":
        print("Please set your API token in the script!")
        return
    
    # Initialize API client
    api = Document360API(API_TOKEN)
    
    print("="*60)
    print("Document360 API - Drive Folder CRUD Operations")
    print("="*60)
    
    # 1. Get all folders
    print("\n1. Getting all folders...")
    print("-" * 30)
    api.get_all_folders()
    
    # 2. Create a new folder
    print("\n2. Creating a new folder...")
    print("-" * 30)
    folder_name = f"Test_Folder_{int(time.time())}"
    folder_id = api.create_folder(folder_name, USER_ID)
    
    if folder_id:
        # 3. Update the folder
        print("\n3. Updating folder...")
        print("-" * 30)
        new_name = f"{folder_name}_Updated"
        api.update_folder(folder_id, new_name, USER_ID)
        
        # 4. Delete the folder
        print("\n4. Deleting folder...")
        print("-" * 30)
        api.delete_folder(folder_id)
    else:
        print("Skipping update and delete since folder creation failed")
    
    print("\n" + "="*60)
    print("Done!")
    print("="*60)

if __name__ == "__main__":
    main()