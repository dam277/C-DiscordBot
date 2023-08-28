const { SlashCommandBuilder, spoiler } = require('discord.js');
const spoil = spoiler("This is a spoiler");

module.exports = {
	data: new SlashCommandBuilder()
		.setName('spoiler')
		.setDescription('Replies with a spoiler'),
	async execute(interaction) {
		await interaction.reply(spoil);
	},
};

