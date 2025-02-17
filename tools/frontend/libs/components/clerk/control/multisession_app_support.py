import reflex as rx


class MultisessionAppSupport(rx.Component):
    library = "@clerk/clerk-react"
    tag = "MultisessionAppSupport"


multisession_app_support = MultisessionAppSupport.create
