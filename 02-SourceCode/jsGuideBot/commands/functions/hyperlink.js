const { SlashCommandBuilder, hyperlink } = require('discord.js');
const link = hyperlink("Portfolio", "https://dam277.github.io/P-Portfolio/#/", "PorftfolioDL");

module.exports = {
	data: new SlashCommandBuilder()
		.setName('hyperlink')
		.setDescription('Replies with a website'),
	async execute(interaction) {
		await interaction.reply(link);
	},
};

