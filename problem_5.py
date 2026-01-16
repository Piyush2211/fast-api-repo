
import python_weather
import asyncio

async def temprature_calulator ():
    
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        
        weather = await client.get("Chandigarh")
        
       
        for daily in weather:
            
            for hourly in daily:
                
                return hourly.kind._name_

if __name__ == "__main__":
    today_temprature = asyncio.run(temprature_calulator())
    # print(today_temprature)
    if(today_temprature == "SUNNY"):
        print("go for a walk: "+today_temprature)
    elif(today_temprature == "RAINY"):
        print("Read a book"+today_temprature)
    elif(today_temprature =="LIGHT_SNOW"):
        print("Create a snow man"+today_temprature)
    else:
        print("Be happy"+today_temprature)
    