from typing import Any, Dict
from imdbpie import Imdb
import lyricwikia
from weather import Weather
from zulip_bots.bots.TimePass import utils, sps, mindGame, hangman, scrabble, todo, calculator, news
import os
from wit import Wit
client = Wit('VMPD5FWPJO6QB7XVP5OKWR4TMHJFKZ75')


class TimePass(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        return '''Build with python and Zulip chat api, Jarvis Bot is the most feature rich unofficial Zulip chat bot that is 100% free and open source.'''

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        results = []
        query = ""
        if message["content"] == "" or message["content"] == "@jarvis help":
            results.append(utils.HELP_MESSAGE)

        data = message["content"].split()
        if(len(data) >= 2 and data[0] == "@jarvis"):
            query = data[1]

        addData = ''
        if data.__len__() > 3:
            addData = data[3]

        if query == "movies":
            results.append(self.query_movie(data[2], addData))
        elif query == "weather":
            dataTemp = data[2::]
            dataTemp = " ".join(dataTemp)
            results.append(self.query_weather(dataTemp))
        elif query == "lyrics":
            dataTemp = data[3::]
            dataTemp = " ".join(dataTemp)
            results.append(self.query_lyrics(data[2],dataTemp))
        elif query == "man":
            results.append(self.query_man(data[2]))
        elif query == "ssh":
            dataTemp = data[5::]
            dataTemp = " ".join(dataTemp)
            results.append(self.query_ssh(data[2],data[3],data[4],dataTemp))
        elif query == "sps":
            results.append(sps.get_sps_response(message, bot_handler))
        elif query == "mind-game":
        	results.append(mindGame.get_mindGame_response(message,bot_handler))
        elif query == "hangman":
        	results.append(hangman.get_response(message,bot_handler))
        elif query == "scrabble":
        	results.append(scrabble.get_response(message,bot_handler))
        elif query == "todo":
        	results.append(todo.get_todo_response(message,bot_handler))
        elif query == "calculator":
            results.append(calculator.get_calculator_response(message,bot_handler))
        elif query == "news":
            results.append(news.get_news_response(message,bot_handler))
        else:
            dataTemp = data[1::]
            dataTemp = " ".join(dataTemp)
            print(dataTemp)
            witAnalysis = client.message(dataTemp)
            print(witAnalysis)
            temp = witAnalysis['entities']
            if temp.__len__() == 0:
                results.append('Sorry :( I could not understatnd what you want to say. Try "@jarvis help" to get detailed help ')
            else:
                trait = witAnalysis['entities']['intent'][0]['value']
                if   trait == "hello":
                    results.append("Hello I am Jarvis nice to meet you !!!! :)")
                elif trait == "bye":
                    results.append("Good bye see you soon :)")
                elif trait == "add-todo":
                    results.append('To add a todo make a query as follows "@jarvis todo add <task to add here>"')
                elif trait == "remove-todo":
                    results.append('To remove a todo make a query as follows "@jarvis todo remove <id of task to remove>"')
                elif trait == "lyrics":
                    results.append('Loving song want to see its lyrics ? Make a query as follows "@jarvis lyrics <composer name> <track name>')
                elif trait == "ssh":
                    results.append('Want to connect to ssh a remote server ? Make a query as follows "@jarvis ssh <user_name> <server_ip> <password> <command>')
                elif trait == "man":
                    results.append('Need some help over usage of command ? make a query as follows "@jarvis man <command>')
                elif trait == "weather":
                    results.append('To get detailed weather report make a query as follows "@jarvis weather <city_name>"')
                elif trait == "calculator":
                    results.append('To start a calculator make a query as follows "@jarvis calculator <computation_to_solve>')
                elif trait == "help":
                    results.append('I think you are stuck try "@jarvis help" to get detailed help about bot')
                elif trait == "list-todo":
                    results.append('To get list of all todos make a query as follows "@jarvis todo list"')
                elif trait == "movies":
                    results.append('Want to get list of all time best movies or maybe details about the celebrity that you like most checkout "@jarvis movies" ')
                elif trait == "scrabble":
                    results.append('Want to play scrabble you are just a query away type "@jarvis scrabble start" to start game')
                elif trait == "sps":
                    results.append('Want to play stone paper scissor you are just a query away type "@jarvis sps start" to start game')
                elif trait == "hangman":
                    results.append('Want to play hangman you are just a query away type "@jarvis scrabble start" to start game')
                elif trait == "memory-game":
                    results.append('Sharpen your memeory by playing some memeory games type "@jarvis memory-game" to start game')
                elif trait == "news":
                    results.append('Get latest news from around the globe just type "@jarvis news <keyword>"')
                elif trait == "cricket":
                    results.append('To get scores of recent matches type "@jarvis cricket"')


        new_content = ''
        for idx, result in enumerate(results, 1):
            new_content += ((str(idx)) if len(results) > 1 else '') + result + '\n'

        bot_handler.send_reply(message, new_content)

    def query_movie(self, query, data):

        imdb = Imdb()
        res = ""
        if query == "popularshows":
            ans = imdb.get_popular_shows()
            for i in range(10):
                res += ans['ranks'][i]['title'] + "\n"
        elif query == "popularmovies":
            ans = imdb.get_popular_movies()
            for i in range(10):
                res += ans['ranks'][i]['title'] + "\n"
        elif query == "search":
            ans = imdb.search_for_title(data)
            for i in range(5):
                res += ans[i]['title'] + "\n"
        return res

    def query_lyrics(self, artist, song):
        return lyricwikia.get_lyrics(artist, song)

    def query_weather(self,city):

        weather = Weather()

        location = weather.lookup_by_location(city)
        res = ""
        forecast = location.forecast()
        for forecasts in forecast:
            res += 'Date: ' + forecasts.date() + '\nCondition: ' + forecasts.text() + '\nHigh Temperature (F): ' + forecasts.high() + '\nLow Temperature (F): ' + forecasts.low() + '\n\n'
        return res

    def query_man(self, command):

        os.system("man " + command + " > man.txt")
        file = open("man.txt","r")
        return file.read()

    def query_ssh(self,user,server,password, command):

        command = "sshpass -p " + password + " ssh " + user + "@" + server + ' "' + command +  '" > output.txt 2>  error.txt'
        os.system(command)
        output = open("output.txt","r")
        error = open("error.txt","r")

        return output.read() + " " + error.read()

handler_class = TimePass