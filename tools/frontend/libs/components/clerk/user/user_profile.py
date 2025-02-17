import reflex as rx


class UserProfile(rx.Component):
    library = "@clerk/clerk-react"
    tag = "UserProfile "


user_profile = UserProfile.create
