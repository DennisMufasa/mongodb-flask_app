'''helper functions for the views'''
def check_user_data(user_data):
    '''a function to ensure user data is all present'''
    user_data_labels = ["username", "password", "email", "role"]

    messsage = ""

    if not user_data:
        return "Enter user information"

    for i in range(len(user_data_labels)):
        if user_data_labels[i] not in user_data:
            messsage = "Missing {}".format(user_data_labels[i])
            return messsage

    return "user data all present"
