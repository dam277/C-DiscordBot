const { SlashCommandBuilder, ChannelType, EmbedBuilder } = require("discord.js");


module.exports = {
    data: new SlashCommandBuilder()
	.setName('validation')
	.setDescription('Replies with your input!')
	.addStringOption(option =>
		option.setName('input')
			.setDescription('The input to echo back')
			// Ensure the text will fit in an embed description, if the user chooses that option
			.setMaxLength(30))
	.addChannelOption(option =>
		option.setName('channel')
			.setDescription('The channel to echo into')
			// Ensure the user can only select a TextChannel for output
			.addChannelTypes(ChannelType.GuildText))
	.addBooleanOption(option =>
		option.setName('embed')
			.setDescription('Whether or not the echo should be embedded')),
        async execute(interaction) 
        {        
            const input = interaction.options.getString('input');
            const channeltype = interaction.options.getChannel('channel');
            const embed = interaction.options.getBoolean('embed');

            console.log(input);
            console.log(channeltype);
            console.log(embed);

            if (embed) 
            {
                // inside a command, event listener, etc.
                const exampleEmbed = new EmbedBuilder()
                .setColor(0x0099FF)
                .setTitle('Some title')
                .setURL('https://discord.js.org/')
                .setAuthor({ name: 'Some name', iconURL: 'https://i.imgur.com/AfFp7pu.png', url: 'https://discord.js.org' })
                .setDescription('Some description here')
                .setThumbnail('https://i.imgur.com/AfFp7pu.png')
                .addFields(
                    { name: 'Regular field title', value: 'Some value here' },
                    { name: '\u200B', value: '\u200B' },
                    { name: 'Inline field title', value: 'Some value here', inline: true },
                    { name: 'Inline field title', value: 'Some value here', inline: true },
                )
                .addFields({ name: 'Inline field title', value: 'Some value here', inline: true })
                .setImage('https://i.imgur.com/AfFp7pu.png')
                .setTimestamp()
                .setFooter({ text: 'Some footer text here', iconURL: 'https://i.imgur.com/AfFp7pu.png' });
                await interaction.reply({embeds: [exampleEmbed]});
            }
            else
                await interaction.reply(`You chosed ${input} ${channeltype} ${embed}`);
        },
    };
    