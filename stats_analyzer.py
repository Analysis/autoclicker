from lxml import html
import requests
import numpy as np
import matplotlib.pyplot as plt

class Runescape:
    def __init__(self, rs_name="lynx titan"):
        self.name = rs_name
        self.stats = self.grab_stats_changes(self.name)
        self.generate_skills(self.stats)
    
    def grab_stats_changes(self,rs_name="lynx titan",rs_time=1):
        name = 'player=' + rs_name
        time = 'time=' + str(rs_time) + 'd'
        api_url = 'https://crystalmathlabs.com/tracker/api.php?type=track'
        page = requests.get(api_url + '&' + name + '&' + time)
        tree = html.fromstring(page.content)
        return tree.xpath('//body//text()')[0].split("\n")[1:]
        
    def update_stats(self):
        api_url = 'https://crystalmathlabs.com/tracker/api.php?type=update'
        name = 'player=' + self.name
        page = requests.get(api_url + '&' + name)
        tree = html.fromstring(page.content)
        
    def generate_skills(self,data):
        self.total = map(int,data[0].split(','))
        self.attack = map(int,data[1].split(','))
        self.defence = map(int,data[2].split(','))
        self.strength = map(int,data[3].split(','))
        self.hitpoints = map(int,data[4].split(','))
        self.range = map(int,data[5].split(','))
        self.prayer = map(int,data[6].split(','))
        self.magic = map(int,data[7].split(','))
        self.cooking = map(int,data[8].split(','))
        self.woodcutting = map(int,data[9].split(','))
        self.fletching = map(int,data[10].split(','))
        self.fishing = map(int,data[11].split(','))
        self.firemaking = map(int,data[12].split(','))
        self.crafting = map(int,data[13].split(','))
        self.smithing = map(int,data[14].split(','))
        self.mining = map(int,data[15].split(','))
        self.herblore = map(int,data[16].split(','))
        self.agility = map(int,data[17].split(','))
        self.thieving = map(int,data[18].split(','))
        self.slayer = map(int,data[19].split(','))
        self.farming = map(int,data[20].split(','))
        self.runecrafting = map(int,data[21].split(','))
        self.hunter = map(int,data[22].split(','))
        self.construction = map(int,data[23].split(','))
    
    def time_to_99(self,skill,xp_per_day):
        return (13034431.0 - skill[2])/xp_per_day
        
    def plot_skill(self,skill_index,days):
        # skill index can be 0 to 23. see generate_skills method above
        data_points = [None] * days
        for i,data in enumerate(data_points):
            stats = self.grab_stats_changes(self.name,days-i)
            data_points[i] = map(int, stats[skill_index].split(','))[2] - map(int, stats[skill_index].split(','))[0]
        
        plt.plot(data_points,marker='o')
        plt.grid(True)
        plt.show()  
            
            
        
        
        
# declase class by giving it a username to track
levon = Runescape('levonski')

# update latest stats
levon.update_stats()

# example calls
print levon.total
print levon.strength
print levon.farming

print levon.time_to_99(levon.strength,250000)

        






