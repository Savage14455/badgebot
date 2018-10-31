from header import *
async def challenge(message, args):
  if args.lower().strip() == 'help':
    await client.send_message(message.channel, help_gym)
    return
  userid = message.author.id
  cursor.execute(lp_select_str, (userid,))
  result = cursor.fetchone()
  cursor.execute(recent_challenge_select_str, (userid,))
  recent_time = cursor.fetchone()[0]
  curent_time = message.timestamp.timestamp()
  if result == None:
    msg = 'You do not have a league pass. Create one with !setlp'
  else:
    cursor.execute(open_challenge_select_str, (userid,))
    result = cursor.fetchone()
    if result != None:
      msg = 'You have an open ' + result[1] + ' challenge'
    elif len(args) == 0:
      msg = 'You do not have an active challenge'
    elif current_time - recent_time < (19*60*60):
      msg = 'Your last challenge was too recent. Please wait 20 hours between challenges'
    elif isbadge(args):
      cursor.execute(challenge_str, (userid, int(current_time, args))
      connection.commit()
      msg = 'Challenge Submitted!'
    else:
      msg = args + ' is not a valid badge'
  await client.send_message(message.channel, msg)
