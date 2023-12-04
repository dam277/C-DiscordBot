const { SlashCommandBuilder } = require("discord.js");

module.exports = {
    data: new SlashCommandBuilder()
	.setName('info')
	.setDescription('Get info about a user or a server!')
	.addSubcommand(subcommand =>
		subcommand
			.setName('user')
			.setDescription('Info about a user')
			.addUserOption(option => option.setName('target').setDescription('The user')))
	.addSubcommand(subcommand =>
		subcommand
			.setName('server')
			.setDescription('Info about the server')),
        async execute(interaction) 
        {  
            const subcommand = interaction.options.getSubcommand(); // Get the selected subcommand

            if (subcommand === 'user') {
                const userOption = interaction.options.getUser('target'); // Get the user object
                if (userOption) {
                    const username = userOption.username;
                    const userId = userOption.id;
                    await interaction.reply(`You chose user: ${username} (ID: ${userId})`);
                } else {
                    await interaction.reply('User not found.');
                }
            } else if (subcommand === 'server') {
                // Code to retrieve server info
                await interaction.reply(`This server is ${interaction.guild.name} and has ${interaction.guild.memberCount} members.`);
            }
        },
    };