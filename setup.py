from cx_Freeze import setup,Executable

base = None

setup(name="Data Mining Game",
		 options={"build_exe":{"packages":["pygame","random","efficient_apriori","re","collections"],
		 					"include_files":["bgm.mp3","objects.txt","assets","difficulty"]}},
         version="1.0",
         description="as above",
         executables=[Executable("game.py", base=base)])
