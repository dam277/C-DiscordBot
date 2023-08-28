const { SlashCommandBuilder } = require("discord.js");


module.exports = {
    data: new SlashCommandBuilder()
    .setName('gif')
    .setDescription('Sends a random gif!')
    .addStringOption(option =>
        option.setName('category')
            .setDescription('The gif category')
            .setRequired(true)
            .addChoices
            (
                { name: 'Funny', value: 'gif_funny' },
                { name: 'Meme', value: 'gif_meme' },
                { name: 'Movie', value: 'gif_movie' },
            )),
        async execute(interaction) 
        {        
            const choice = interaction.options.getString('category');
            console.log(choice);
            await interaction.reply(`You chosed ${choice}`);
        },
    };