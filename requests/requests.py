TOKEN = ''

import requests
import json

PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'ITERATOR', 'REQUESTS']
GROUP = ['1021', '1022']
ACTION = ['Added', 'Deleted', 'Refactored', 'Moved']

def prepare_headers():
  return{'Authorization': 'Token {}'.format(TOKEN),
         'Content-Type': "application/json",
         'Accept': "application/vnd.github.v3+json"
        }

def get_all_user_pull_reqs(user_name, repos_name, state):
  url = 'https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_name, repos_name, state)
  all_pr = requests.get(url, headers=prepare_headers())
  return all_pr

def get_all_pr_commits(pull_req):
  all_commits = requests.get(pull_req['commits_url'], headers=prepare_headers())
  return all_commits

def check_comment(message):
  res = []
  mass = []
  mass = message.split('-')
  pre = mass[0]
  post = mass[1].split(' ')
  if pre not in PREFIX:
    res.append("The prefix of your comment must be from {}".format(PREFIX))
  if post[0] not in GROUP:
    res.append("Number of your group must be from {}".format(GROUP))
  if len(post) > 1 and post[1] not in ACTION:
    res.append("Action of your comment must be from {}".format(ACTION))
  return '\n'.join(res)

def create_message(pull_req):
  message = "Your pull request: {}\n".format(pull_req['title'])
  message += check_comment(pull_req['title'])
  message += '\n\n'
  for com in get_all_pr_commits(pull_req).json():
    comm = com['commit']
    message += 'Your commit: {}\n'.format(comm['message'])
    message += check_comment(comm['message'])
    message += '\n'
  return message

def send_message(pull_req, message):
  data = {'body': message,
          'path': requests.get(pull_req['url']+'/files', headers=prepare_headers()).json()[0]['filename'],
          'position': 1,
          'commit_id': pull_req['head']['sha']}
  r = requests.post(pull_req['url']+'/comments', headers=prepare_headers(), json=data)
  print(r.json())

def main():
  for pr in get_all_user_pull_reqs('OcTatiana', 'python_au', 'open').json():
    if len(create_message(pr)) > 200:
      send_message(pr, create_message(pr))

main()