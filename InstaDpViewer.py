#pip install instaloader
import instaloader
 
ig = instaloader.Instaloader()
DP = input("Enter Insta username : ")
 
ig.download_profile(dp , profile_pic_only=True)
print("Your Image is Downloaded")