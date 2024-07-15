# Team Revolution Discord Bot

## General Setup

The First thing to do is run the setup.sh script

```sh
  ./setup.sh

```

The environment needs some variables set in order to function properly.

*API_PORT*: The Http port the web api listens to

*MASTERKEY*: A basic key to authenticate the request (not secure but better than nothing :D)

*TOKEN*: The Discord bot token

## ApiDoc

A request to the API is done by making a post request to the URL of the Server

```sh
    http://localhost/:<PORT>
```

and the json content

```json
{
  "key": "APIKEY",
  "sender": 420,
  "target": 4711,
  "data": {

  }

}
```

*key*: The Api key

*SenderID*: The SenderID is a unique id in order to identify and log the sender of the message

*TargetID*: The TargetID is a unique id to identify the target [see TargetID](#target_ids)

*data*: The data block is special for every target id.

### Send message to Discord

target_id : 1

``` json
{
"channel" : "<INT> discord_channel_id",
"content" :  "<STRING> the message you want to send"
}
```

### Target_Ids

| ID  | Description    |
|-----|----------------|
| 1   | Discord Server |
|     |                |
|     |                |
