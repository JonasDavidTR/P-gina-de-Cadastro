
def processar_dados(googleUser):
    userProfile = googleUser.getBasicProfile()
    userId = ('ID: ' + userProfile.getId())
    userNome = ('Name: ' + userProfile.getName())
    userImage = ('Image URL: ' + userProfile.getImageUrl())
    userEmail = ('Email: ' + userProfile.getEmail())
