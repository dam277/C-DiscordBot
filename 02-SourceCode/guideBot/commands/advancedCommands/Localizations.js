const { SlashCommandBuilder } = require("discord.js");

module.exports = {
    data: new SlashCommandBuilder()
	.setName('dog')
	.setNameLocalizations({
		fr: 'chien',
		de: 'hund',
	})
	.setDescription('Get a cute picture of a dog!')
	.setDescriptionLocalizations({
		fr: 'Obtenir une photo de chien',
		de: 'Poste ein niedliches Hundebild!',
	})
	.addStringOption(option =>
		option
			.setName('breed')
			.setDescription('Breed of dog')
			.setNameLocalizations({
				fr: 'race',
				de: 'rasse',
			})
			.setDescriptionLocalizations({
				fr: 'Race du chien',
				de: 'Hunderasse',
			}),
	),
    async execute(interaction) 
    {        
        const breed = interaction.options.getString('breed');
        await interaction.reply(`You chosed ${breed}`);
    },
};