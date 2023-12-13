from .Database import Database
import mysql.connector as connector

class Server:
    id = None               # Id of the server
    guild_id = None         # Id of the guild
    name = None             # Name of the server

    TABLE = "server"

    def __init__(self, id, guild_id, name):
        self.id = id
        self.guild_id = guild_id
        self.name = name

    @staticmethod
    async def create_server(guild_id, name):
        """ Create a server into the database 
        $param guild_id: Guild -> Discord server id
        $param name: string -> Discord server name"""

        # Get the query string
        fields = "(id_server, guildId, name)"
        params = "(%(id_server)s, %(guildId)s, %(name)s)"
        query = f"INSERT INTO {Server.TABLE} {fields} VALUES {params}"

        # Get the server and define if it already exists
        obj_server = await Server.get_server_by_guild_id(guild_id)
        if obj_server is not None:
            return "The server is already created !"
        
        # If the server doesn't exists, insert it into the database
        result = await Database.get_instance().bind_exec(query, {"id_server" : None, "guildId": guild_id, "name": name})
        if result[1] is True:
            message = "Server successfully created !"
        else:
            message = result

        # Return the message to the user
        return message
    
    @staticmethod
    async def get_server_by_guild_id(guild_id):
        """ Get a server by guild id
        $param guild_id: Guild -> Discord server id
        Return format_object()"""

        # Get the query string
        where = "guildId = %(guildId)s"
        query = f"SELECT * FROM {Server.TABLE} WHERE {where}"

        # Get the result by executing query into the database
        result = await Database.get_instance().bind_exec(query, {"guildId": guild_id})
        return Server.format_object(result)
    
    @staticmethod
    def format_object(result):
        """ Format a database result into a object 
        $param result: MySql object -> result of the query 
        Return None | Server -> None for no data, Server for successfully getting data """

        # Getting datas from result
        datas = result[0].fetchall()

        # Check if datas are filled
        if len(datas) < 1:
            return None
        
        # Create a server object and return it
        server = Server(id=datas[0][0], guild_id=datas[0][1], name=datas[0][2])
        return server
    
