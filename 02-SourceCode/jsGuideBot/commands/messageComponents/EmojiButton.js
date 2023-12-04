const { SlashCommandBuilder, PermissionFlagsBits, ButtonBuilder, ButtonStyle, ActionRowBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('emojibutton')
		.setDescription('A emoji button'),
        async execute(interaction) {
	
            const emojibutton = new ButtonBuilder()
				.setCustomId('emoji')
				.setLabel("Ouais euh, j'ai fait 12 kills et toi seulement 3")
				.setStyle(ButtonStyle.Primary)
				.setEmoji("🤓");

			const row = new ActionRowBuilder()
				.addComponents(emojibutton);

			await interaction.reply({
				content: `Emojiiiiiiiiiiiiiiiiiiiii !!!`,
				components: [row],
			});
		},
};