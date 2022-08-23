from preprocessing import DF
from streamlitUI import user_interface

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Initialize Web Application
    user_interface(DF, "https://agsi.gie.eu/api?country=DE&company=21X000000001127H")