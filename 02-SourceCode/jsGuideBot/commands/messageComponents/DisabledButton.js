const { SlashCommandBuilder, PermissionFlagsBits, ButtonBuilder, ButtonStyle, ActionRowBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('clickme')
		.setDescription('A button that you can click on'),
        async execute(interaction) {
	
            const disabledButton = new ButtonBuilder()
                .setCustomId('disabled')
                .setLabel('Click me ? hehe you cant')
                .setStyle(ButtonStyle.Primary)
                .setDisabled(true);

			const row = new ActionRowBuilder()
				.addComponents(disabledButton);

			await interaction.reply({
				content: `Try to click this button`,
				components: [row],
			});
		},
};