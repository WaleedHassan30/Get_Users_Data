import time,requests,csv,pandas as pd
    ################################################################################
class script:
    def __init__(self,script_Name,api,data_section,assign_columns=["name","username","email","street","suite","city","zipcode","geo_lat","geo_lng"]):
        self.api = api
        self.script_Name = script_Name
        self.data_section = data_section
        self.assign_columns = assign_columns
        self.save_data = []
        self.data = requests.get(api)
        self.data_json = self.data.json
    ################################################################################
    def Get_Script_Name(self):
        print("Script name is: " , self.script_Name)
    def show_api(self):
        return self.data_json()[self.data_section]
    ################################################################################
    def Save_To_Csv_file(self):
        count = 0
        filename = self.script_Name+"_File"+".csv"
        with open(filename,"w",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=self.assign_columns)
            writer.writeheader()
            for data in self.data_json():     
                for row in range(len(self.data_json())):
                    temp_dict = {"name" : self.data_json()[row]["name"],    
                    "username": self.data_json()[row]["email"],
                    "email" : self.data_json()[row]["email"],
                    "suite" : self.data_json()[row]["address"]["suite"],
                    "city" : self.data_json()[row]["address"]["city"],
                    "zipcode" : self.data_json()[row]["address"]["zipcode"],
                    "geo_lat" : self.data_json()[0]["address"]["geo"]["lat"],
                    "geo_lng" : self.data_json()[0]["address"]["geo"]["lng"]}        
                    writer.writerow(temp_dict)
                    count +=1
                break

        print(f"Done , Exported file {filename} including {count} full users informations " )
        data = pd.read_csv(filename) 
        return data
    ################################################################################