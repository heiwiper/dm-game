from cx_Freeze import Executable, setup

base = None

setup(name="Data Mining Game",
		 options={"build_exe":{"packages":["pygame","random","efficient_apriori","re","collections"],
		 					"include_files":["objects.txt","assets","difficulty"]}},
         version="0.1",
         description="This game implements Apriori algorithm from data mining class.",
         author="Mohammed Benzouache & Abdallah Maouche",
         executables=[Executable("game.py", base=base, icon="icon.ico")])
