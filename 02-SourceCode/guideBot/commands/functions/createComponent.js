const { SlashCommandBuilder, createComponent, ComponentType, Message } = require('discord.js');


module.exports = {
	data: new SlashCommandBuilder()
		.setName('component')
		.setDescription('Replies with a component'),
	async execute(interaction) {
        const component = createComponent(new Message(true, "test"), ComponentType.Message);
        interaction.reply(component);
	},
};

