const { SlashCommandBuilder, PermissionFlagsBits, ButtonBuilder, ButtonStyle, ActionRowBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('buttonlink')
		.setDescription('Select a member and ban them.')
		.addStringOption(option =>
			option
				.setName('title')
				.setDescription('the title of the button')
				.setRequired(true))
        .addStringOption(option =>
            option
                .setName('link')
                .setDescription('The link of the button')
                .setRequired(true)),
        async execute(interaction) {
			const title = interaction.options.getString('title');
			const link = interaction.options.getString('link');
	
			const titleButton = new ButtonBuilder()
				.setLabel(title)
                .setURL(link)
				.setStyle(ButtonStyle.Link);

			const row = new ActionRowBuilder()
				.addComponents(titleButton);

			await interaction.reply({
				content: `This button will redirect you to ${title}`,
				components: [row],
			});
		},
};