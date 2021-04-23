import user_class_privileges

newAdmin = user_class_privileges.Admin("John", "Smith", "JJJS", 104, "UK", "JJJS@shortnamesonly.com", "01/01/2020", "01/01/2020")

newAdmin.privileges.show_privileges()

