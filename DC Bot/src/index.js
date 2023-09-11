require('dotenv').config();
const { PREFIX, DBPool, client } = require("./var_dump.js");
const { DBSeed, ReVoke, DownLoad, inFo, hwidReset, rockStar, linkDiscord, myInfo, TransFer, buyer, genkey} = require("./commands.js");

// CLIENT READY AND BOT ACTIVITY
client.on('ready', () => {
    console.log("Connected as " + client.user.tag);

    client.user.setActivity("FiveM", {type: "PLAYING"});
});

client.on('message', async message => {
    if (message.author.bot) return; 
    if (message.content.startsWith(PREFIX)) { 
            const [CMD_NAME, ...args] = message.content 
            .trim()
            .substring(PREFIX.length)
            .split(/\s+/);
    

            
        if (CMD_NAME === 'generate') DBSeed(message, DBPool);
        if (CMD_NAME === 'download') DownLoad(message,DBPool);
        if (CMD_NAME === 'revoke') ReVoke(message, DBPool);
        if (CMD_NAME === 'info') inFo(message, DBPool);
        if (CMD_NAME === 'hwidreset') hwidReset(message, DBPool);
        if (CMD_NAME === 'rockstar') rockStar(message, DBPool);
        if (CMD_NAME === 'customers') customers(message);
        if (CMD_NAME === 'redeem') linkDiscord(message, DBPool);
        if (CMD_NAME === 'myinfo') myInfo(message, DBPool);
        if (CMD_NAME === 'transfer') TransFer(message, DBPool);
        if (CMD_NAME === 'buyer') buyer(message);
        if (CMD_NAME === 'genkey') genkey(message, DBPool);
    }
});

client.login(process.env.BOT_TOKEN);