const { RANDOM } = require("mysql/lib/PoolSelector");
const { DBLicenseEntry, DBLicenseEntry2 } = require("./helpers");
const { DBPool } = require("./var_dump");
const { client } = require('./var_dump');

const DBSeed = (message, DBPool) => {
  if (message.author.bot) return;
  if (message.author.id !== "696930965678719037" && message.author.id !== "480664548576198676" && message.author.id !== "847937253133254697" && message.author.id !== "884519580855308289" && message.author.id !== "926427801488338944" && message.author.id !== "906982676643348591" && message.author.id !== "942015198858997810" && message.author.id !== "930592099391385611" && message.author.id !== "784681934533165097" && message.author.id !== "780026379924013056" && message.author.id !== "281130408735670272" && message.author.id !== "552801539744464896" && message.author.id !== "473775428545413130" && message.author.id !== "450309451031773184" && message.author.id !== "434747915169431572") return;
  if (message.channel.id == 957333835807354937) {
    let entry = parseInt(message.content.split(" ")[1])
    if (isNaN(entry)) {
      return message.reply("Enter a valid number, try: !!generate number")
    } else {
      if (entry <= 10) {
        DBPool.getConnection(function (err, conn) {
          if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
          console.log('MySQL: Connected to Database');
          isNaN(entry) ? conn.query(DBLicenseEntry(1)) : conn.query(DBLicenseEntry(message, entry))
          console.log(entry)
        })
      }
      else {
        return message.reply("Don't generate in such high numbers please.")
      }
      ;
    }
  }
}

const genkey = (message, DBPool) => {
  entry = 1;
  if (message.author.bot) return;
  if (message.author.id !== "926427801488338944" && message.author.id !== "847937253133254697" && message.author.id !== "405294799692890113") return;
  DBPool.getConnection(function (err, conn) {
    if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
    console.log('MySQL: Connected to Database');
    isNaN(entry) ? conn.query(DBLicenseEntry2(1)) : conn.query(DBLicenseEntry2(message, entry))
    console.log(entry)
  })
    ;
}

const ReVoke = (message, DBPool) => {
  if (message.author.bot) return;
  if (message.author.id !== "847937253133254697" && message.author.id !== "926427801488338944" && message.author.id !== "535926829672955904" && message.author.id !== "567759491039363152" && message.author.id !== "602809480077377537" && message.author.id !== "738106671833808947") return;
  let keyje = message.content.split(" ")[1]
  if (keyje == null && keyje == "") { conn.release(); }
  DBPool.getConnection(function (err, conn) {
    if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
    console.log('MySQL: Connected to Database');
    console.log("revoked: ", keyje);
    conn.query("UPDATE `keys` SET `UUID`='revoked' WHERE `key`=?", [message.content.split(" ")[1]])
    message.reply('Changed status of that key to "revoked"')

  });
}

const hwidReset = (message, DBPool) => {
  if (message.author.bot) return;
  if (message.author.id !== "847937253133254697" && message.author.id !== "926427801488338944" && message.author.id !== "535926829672955904" && message.author.id !== "474885672847802368" && message.author.id !== "738106671833808947") return;
  let keyje = message.content.split(" ")[1]
  if (keyje == null && keyje == "") { conn.release(); }
  DBPool.getConnection(function (err, conn) {
    if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
    console.log('MySQL: Connected to Database');
    console.log("hwidreset: ", keyje);
    conn.query("UPDATE `keys` SET `UUID`='none' WHERE `key`=?", [message.content.split(" ")[1]])
    message.reply('Hwid resetted of that key!')

  });
}


const inFo = (message, DBPool) => {
  if (message.author.bot) return;
  if (message.author.id !== "405294799692890113" && message.author.id !== "847937253133254697" && message.author.id !== "926427801488338944" && message.author.id !== "535926829672955904" && message.author.id !== "738106671833808947" && message.author.id !== "474885672847802368" && message.author.id !== "729739686116851802") return;
  let keyje = message.content.split(" ")[1]
  if (keyje == null && keyje == "") { conn.release(); }
  DBPool.getConnection(function (err, conn) {
    if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
    console.log('MySQL: Connected to Database');
    console.log(keyje)
    conn.query("SELECT * FROM `keys` WHERE `key`=?", [message.content.split(" ")[1]], (err, result, fields) => {
      if (err) return console.log(err)
      if (!result || result.length <= 0) {
        conn.query("SELECT * FROM `keys` WHERE `discordid`=?", [message.content.split(" ")[1]], (err, result, fields) => {
          if (!result || result.length <= 0) { return message.channel.send('Not found') }
          else {
            console.log(result[0])
            message.reply('Information can be found in your DM!')
            message.author.send("Information about that key:")
            message.author.send("```" + `Hwid: ${result[0].UUID} \nKey: ${result[0].key} \nDiscordID: ${result[0].discordid}` + "```")
          }
        })

      } else {
        console.log(result[0])
        message.reply('Information can be found in your DM!')
        message.author.send("Information about that key:")
        message.author.send("```" + `Hwid: ${result[0].UUID} \nKey: ${keyje} \nDiscordID: ${result[0].discordid}` + "```")
      }
    })

  });
}

const rockStar = (message, DBPool) => {
  if (message.author.bot) return;
  if (message.author.id !== "847937253133254697" && message.author.id !== "926427801488338944" && message.author.id !== "535926829672955904") return;
  DBPool.getConnection(function (err, conn) {
    if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
    console.log('MySQL: Connected to Database');
    conn.query("SELECT `account` FROM `rockstar` ORDER BY RAND() LIMIT 1", (err, result, fields) => {
      account = result[0].account;
      console.log("Generated account: " + result[0].account)
      if (err) return console.log(err)
      conn.query("DELETE FROM `rockstar` WHERE `account`=?", [account], (err, resultss, fields) => {
        if (err) return console.log(err)
        message.reply('You can find your rockstar account in your PM!')
        message.author.send("Here is your rockstar account BOSS!")
        message.author.send("```" + `Account: ${account}` + "```")
      })
    });
  })
}

const linkDiscord = (message, DBPool) => {
  if (message.channel.id == 957333834930720778 || message.channel.id == 953761240851836948 || message.channel.id == 961269754251849738) {
    if (message.author.bot) return;
    let discordidd = message.author.id;
    let keyje = message.content.split(" ")[1]
    if (keyje == null && keyje == "") {
      message.reply("Please follow the template: !!redeem key")
    } else {
      DBPool.getConnection(function (err, conn) {
        if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
        console.log('MySQL: Connected to Database');
        conn.query("SELECT `discordid` FROM `keys` WHERE `key`=?", [message.content.split(" ")[1]], (err, resultsss, fields) => {
          if (err) return console.log(err)
          if (!resultsss || resultsss.length <= 0) {
            return message.channel.send('Key not found')
          } else {
            console.log(resultsss[0].discordid)
            if (resultsss[0].discordid == null) {
              console.log(resultsss[0].discordid)
              message.author.send('Steps: https://docs.google.com/spreadsheets/d/1ZTYK_JhWDCiTmDN5YGvJkvwF511TgIQ1H-F6kkaBKl4/edit#gid=167096642').catch(() => message.reply("Sorry your dms are off!"));
              message.reply("You succesfully linked your discord with this key.")
              conn.query("UPDATE `keys` SET `discordid`=? WHERE `key`=?", [discordidd, message.content.split(" ")[1]])
            } else if (resultsss[0].discordid == discordidd) {
              message.reply("You are already linked to this key.")
            }
            else {
              console.log(resultsss[0].discordid)
              message.reply("Key already linked with: <@" + resultsss[0].discordid + ">")
            }
          }
        })

      });
    }
  }
}


const myInfo = (message, DBPool) => {
  if (message.author.bot) return;
  if (message.channel.id == 957333834930720778) {
    DBPool.getConnection(function (err, conn) {
      if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
      console.log('MySQL: Connected to Database');

      conn.query("SELECT `key` FROM `keys` WHERE `discordid` = ?", [message.author.id], (err, result, fields) => {
        if (result[0]) {
          message.reply(`Here is you're information:\n` + "```" + `Key: ${result[0].key}\nLicense: Lifetime ` + "```")
        }
        else return message.reply('You have no license registered in the database.')
      })
    });
  }
}

const TransFer = (message, DBPool) => {
  if (message.channel.id == 957333834930720778) {
    let newid = message.content.split(" ")[1]
    if (newid == null && newid == "" && newid == "undefined") { conn.release(); }
    DBPool.getConnection(function (err, conn) {
      if (err) { conn.release(); console.log('MySQL: Pool connection error: ' + err); }
      console.log('MySQL: Connected to Database');
      conn.query("SELECT `key` FROM `keys` WHERE `discordid` = ?", [message.author.id], (err, resultssss, fields) => {
        if (!resultssss || resultssss.length <= 0) { return message.reply('You have no license registered in the database.') }
        conn.query("UPDATE `keys` SET `discordid`=? WHERE `discordid`=?", [newid, message.author.id])
        message.reply(" You're license has been transfered to <@" + newid + ">")
        client.channels.cache.get(`943209284106354749`).send(`<@${message.author.id}> has transfered his license to <@${newid}>`)

      })
    })
  }
}



const DownLoad = (message, DBPool) => {
  DBPool.getConnection(function (err, conn) {
    if (message.channel.id == 957333834930720778 || message.channel.id == 953761240851836948 || message.channel.id == 961269754251849738) {
      conn.query("SELECT `key` FROM `keys` WHERE `discordid` = ?", [message.author.id], (err, resultssss, fields) => {
        if (!resultssss || resultssss.length <= 0) { return message.reply('You have no license registered in the database.') }
        message.reply('you can find the download link in your pm!')
        message.author.send('https://cdn.discordapp.com/attachments/926437655812657152/955176074306805800/Storm_Sp00fer_V2.1.exe').catch(() => message.reply("Sorry your dms are off!"));
      })
    }
  })
}

const buyer = (message) => {
  if (message.author.id !== "847937253133254697" && message.author.id !== "926427801488338944" && message.author.id !== "405294799692890113" && message.author.id !== "729739686116851802") return;
  const embed = {
    "description": "Thank you for buying Storm Sp00fer",
    "color": 0x7b00ff,
    "footer": {
      "text": "2022 - Storm Sp00fer"
    },
    "thumbnail": {
      "url": "https://cdn.discordapp.com/attachments/939999798260551691/940016724986724393/Comp_1_305_1.png"
    },
    "author": {
      "name": "Storm Sp00fer",
      "url": "https://discord.gg/stormsp00fer"
    },
    "fields": [
      {
        "name": "How to activate?",
        "value": "!!redeem <yourkey> \n !!download \n in the <#957333834930720778> channel."
      }
    ]
  };
  message.reply({ embed })
}





function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}


module.exports = { DBSeed, DownLoad, ReVoke, inFo, hwidReset, rockStar, linkDiscord, myInfo, TransFer, buyer, genkey}; 