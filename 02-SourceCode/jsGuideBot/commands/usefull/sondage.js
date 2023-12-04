const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageActionRow, MessageButton } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('sondage')
        .setDescription('Crée un sondage avec des boutons de réponse.')
        .addStringOption(option =>
            option.setName('question')
                .setDescription('La question du sondage.')
                .setRequired(true))
        .addStringOption(option =>
            option.setName('reponse1')
                .setDescription('Première réponse.')
                .setRequired(true))
        .addStringOption(option =>
            option.setName('reponse2')
                .setDescription('Deuxième réponse.')
                .setRequired(true))
        .addStringOption(option =>
            option.setName('reponse3')
                .setDescription('Troisième réponse.')
                .setRequired(true)),
        async execute(interaction) {
            const question = interaction.options.getString('question');
            const reponse1 = interaction.options.getString('reponse1');
            const reponse2 = interaction.options.getString('reponse2');
            const reponse3 = interaction.options.getString('reponse3');
        
            const row = new MessageActionRow()
                .addComponents(
                    new MessageButton()
                        .setCustomId('reponse1')
                        .setLabel(reponse1)
                        .setStyle('PRIMARY'),
                    new MessageButton()
                        .setCustomId('reponse2')
                        .setLabel(reponse2)
                        .setStyle('PRIMARY'),
                    new MessageButton()
                        .setCustomId('reponse3')
                        .setLabel(reponse3)
                        .setStyle('PRIMARY'),
                );
        
            await interaction.reply({ content: question, components: [row] });
        },
};