const { client } = require('./var_dump');

require('dotenv').config();
function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}
function rScriptsv1() {
    const scriptrotation = ['none', 'none', 'none'];

    return scriptrotation[Math.floor(Math.random() * scriptrotation.length)]
}

function DBLicenseEntry(message, entries) {
    let sqlitems = [], sql
    console.log("generating entries");

    for (i = 1; i <= entries; i++) {
        sqlitems.push({ id: uuidv4(), script: rScriptsv1() });
    }
    console.log("entries have been generated");
    console.log("preparing SQL statement");
    message.author.send('Hi my king, here are your beloved key(s)')
    sql = "INSERT INTO `keys` (`key`, `UUID`) VALUES"
    sqlitems.map((item, index) => {
        index === 0 ? sql += ` ('${item.id}', '${item.script}')` : sql += `, ('${item.id}', '${item.script}')`
        message.author.send("```Lifetime key: " + item.id + "```")
        client.channels.cache.get(`935552478798299246`).send(`Key: ${item.id} has been generated by: <@${message.author.id}> `)
    });
    message.reply('you can find the keys in your pm!')
    console.log("sql prepared")
    return sql;
}

function DBLicenseEntry2(message, entries) {
    let sqlitems = [], sql
    console.log("generating entries");

    for (i = 1; i <= entries; i++) {
        sqlitems.push({ id: uuidv4(), script: rScriptsv1() });
    }
    console.log("entries have been generated");
    console.log("preparing SQL statement");
    sql = "INSERT INTO `keys` (`key`, `UUID`) VALUES"
    sqlitems.map((item, index) => {
        index === 0 ? sql += ` ('${item.id}', '${item.script}')` : sql += `, ('${item.id}', '${item.script}')`
        message.reply("```Lifetime key: " + item.id + "```")
        client.channels.cache.get(`935552478798299246`).send(`Key: ${item.id} has been generated by: <@${message.author.id}> `)
    });
    console.log("sql prepared")
    return sql;
}

module.exports = { DBLicenseEntry, DBLicenseEntry2 };