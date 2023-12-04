const { SlashCommandBuilder, StringSelectMenuBuilder, StringSelectMenuOptionBuilder, ActionRowBuilder, UserSelectMenuBuilder, RoleSelectMenuBuilder, MentionableSelectMenuBuilder, ChannelType, ChannelSelectMenuBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('select')
		.setDescription('A selector')
            .addStringOption(option =>
                option.setName('selectortype')
                    .setDescription('The selector type')
                    .setRequired(true)
                    .addChoices
                    (
                        { name: 'Classic', value: "0" },
                        { name: 'User', value: "1" },
                        { name: 'Role', value: "2" },
                        { name: 'Mentionable', value: "3" },
                        { name: 'Channel', value: "4" },
                    )),
        async execute(interaction) {

            let select;
            switch(interaction.options.getString("selectortype"))
            {
                case "0":
                    select = new StringSelectMenuBuilder()
                        .setCustomId('starter')
                        .setPlaceholder('Chose your starter')
                        .addOptions(
                            new StringSelectMenuOptionBuilder()
                                .setLabel('Bulbasaur')
                                .setDescription('The dual-type Grass/Poison Seed Pokémon.')
                                .setValue('bulbasaur')
                                .setDefault(true),
                            new StringSelectMenuOptionBuilder()
                                .setLabel('Charmander')
                                .setDescription('The Fire-type Lizard Pokémon.')
                                .setValue('charmander'),
                            new StringSelectMenuOptionBuilder()
                                .setLabel('Squirtle')
                                .setDescription('The Water-type Tiny Turtle Pokémon.')
                                .setValue('squirtle'),
                        );
                    break;
                case "1": 
                    select = new UserSelectMenuBuilder()
                        .setCustomId('user')
                        .setPlaceholder('Select one or two users')
                        .setMinValues(1)
                        .setMaxValues(2);
                    break;
                case "2": 
                    select = new RoleSelectMenuBuilder()
                        .setCustomId('role')
                        .setPlaceholder('Select one or two roles')
                        .setMinValues(1)
                        .setMaxValues(2);
                    break;
                case "3": 
                    select = new MentionableSelectMenuBuilder()
                        .setCustomId('mentionable')
                        .setPlaceholder('Select one or two mentionables')
                        .setMinValues(1)
                        .setMaxValues(2);
                    break;
                case "4": 
                    select = new ChannelSelectMenuBuilder()
                        .setCustomId('channel')
                        .setChannelTypes(ChannelType.GuildVoice)
                        .setPlaceholder('Select one or two channels')
                        .setMinValues(1)
                        .setMaxValues(2);
                break;
            }
    
            const row = new ActionRowBuilder()
                .addComponents(select);
    
            await interaction.reply({
                content: 'Choose an option',
                components: [row],
            });
        },
    }