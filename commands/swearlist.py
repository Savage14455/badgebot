from header import *
async def swearlist(message, args):
  user = getmention(message, args, message.server)
  if user == None:
    await client.send_message(message.channel, 'There is no one on this server named ' + args)
    return
  limit = 0
  if len(args)==0:
    cursor.execute(swear_dump_str, (limit,))
    results = cursor.fetchall()
    ids = [results[0][0]]
    count = results[0][1]
    i = 1
    dump = ''
    while i < len(results) and count > 0:
      if results[i][1] == count:
        ids.append(results[i][0])
      else:
        dump += str(count) + ' - ' + ', '.join(list(filter(lambda y: y != None, [id_to_discordname(x, client.get_server('372042060913442818')) for x in ids]))) + '\n'
        ids = [results[i][0]]
        count = results[i][1]
      i+=1
    dump += str(count) + ' - ' + ', '.join(list(filter(lambda y: y != None, [id_to_discordname(x, client.get_server('372042060913442818')) for x in ids]))) + '\n'

  else:
    cursor.execute(swear_select_str, (discorduser_to_id(user),))
    result = cursor.fetchone()
    if result == None or result[0] == None:
      dump = '0'
    else:
      dump = str(result[0])
  await client.send_message(message.channel, dump)
