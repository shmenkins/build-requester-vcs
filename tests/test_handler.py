import os
import boto3
import main
import json
from mock import MagicMock
from mock import patch
from mock import ANY

region = boto3.session.Session().region_name
account = boto3.client("sts").get_caller_identity().get("Account")

# payload is stored as a string in the event body
github_webhook_payload_string = json.dumps({
  "ref": "refs/heads/master",
  "before": "5267c0c79a739cfc3ee69e892ade78871753fc8a",
  "after": "856c2c2e39a4ffadba2501df2c7dcf6b56b16543",
  "created": False,
  "deleted": False,
  "forced": False,
  "base_ref": None,
  "compare": "https://github.com/rzhilkibaev/cfgen/compare/5267c0c79a73...856c2c2e39a4",
  "commits": [
    {
      "id": "856c2c2e39a4ffadba2501df2c7dcf6b56b16543",
      "tree_id": "dfeb02523b7f7e275a0e8c84cee5c3a30df700ca",
      "distinct": True,
      "message": "Create delete-me",
      "timestamp": "2017-04-23T01:41:52-07:00",
      "url": "https://github.com/rzhilkibaev/cfgen/commit/856c2c2e39a4ffadba2501df2c7dcf6b56b16543",
      "author": {
        "name": "Renat",
        "email": "rzhilkibaev@users.noreply.github.com",
        "username": "rzhilkibaev"
      },
      "committer": {
        "name": "GitHub",
        "email": "noreply@github.com",
        "username": "web-flow"
      },
      "added": [
        "delete-me"
      ],
      "removed": [

      ],
      "modified": [

      ]
    }
  ],
  "head_commit": {
    "id": "856c2c2e39a4ffadba2501df2c7dcf6b56b16543",
    "tree_id": "dfeb02523b7f7e275a0e8c84cee5c3a30df700ca",
    "distinct": True,
    "message": "Create delete-me",
    "timestamp": "2017-04-23T01:41:52-07:00",
    "url": "https://github.com/rzhilkibaev/cfgen/commit/856c2c2e39a4ffadba2501df2c7dcf6b56b16543",
    "author": {
      "name": "Renat",
      "email": "rzhilkibaev@users.noreply.github.com",
      "username": "rzhilkibaev"
    },
    "committer": {
      "name": "GitHub",
      "email": "noreply@github.com",
      "username": "web-flow"
    },
    "added": [
      "delete-me"
    ],
    "removed": [

    ],
    "modified": [

    ]
  },
  "repository": {
    "id": 72402842,
    "name": "cfgen",
    "full_name": "rzhilkibaev/cfgen",
    "owner": {
      "name": "rzhilkibaev",
      "email": "rzhilkibaev@users.noreply.github.com",
      "login": "rzhilkibaev",
      "id": 3160853,
      "avatar_url": "https://avatars1.githubusercontent.com/u/3160853?v=3",
      "gravatar_id": "",
      "url": "https://api.github.com/users/rzhilkibaev",
      "html_url": "https://github.com/rzhilkibaev",
      "followers_url": "https://api.github.com/users/rzhilkibaev/followers",
      "following_url": "https://api.github.com/users/rzhilkibaev/following{/other_user}",
      "gists_url": "https://api.github.com/users/rzhilkibaev/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/rzhilkibaev/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/rzhilkibaev/subscriptions",
      "organizations_url": "https://api.github.com/users/rzhilkibaev/orgs",
      "repos_url": "https://api.github.com/users/rzhilkibaev/repos",
      "events_url": "https://api.github.com/users/rzhilkibaev/events{/privacy}",
      "received_events_url": "https://api.github.com/users/rzhilkibaev/received_events",
      "type": "User",
      "site_admin": False
    },
    "private": False,
    "html_url": "https://github.com/rzhilkibaev/cfgen",
    "description": "Config for config",
    "fork": False,
    "url": "https://github.com/rzhilkibaev/cfgen",
    "forks_url": "https://api.github.com/repos/rzhilkibaev/cfgen/forks",
    "keys_url": "https://api.github.com/repos/rzhilkibaev/cfgen/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/rzhilkibaev/cfgen/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/rzhilkibaev/cfgen/teams",
    "hooks_url": "https://api.github.com/repos/rzhilkibaev/cfgen/hooks",
    "issue_events_url": "https://api.github.com/repos/rzhilkibaev/cfgen/issues/events{/number}",
    "events_url": "https://api.github.com/repos/rzhilkibaev/cfgen/events",
    "assignees_url": "https://api.github.com/repos/rzhilkibaev/cfgen/assignees{/user}",
    "branches_url": "https://api.github.com/repos/rzhilkibaev/cfgen/branches{/branch}",
    "tags_url": "https://api.github.com/repos/rzhilkibaev/cfgen/tags",
    "blobs_url": "https://api.github.com/repos/rzhilkibaev/cfgen/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/rzhilkibaev/cfgen/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/rzhilkibaev/cfgen/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/rzhilkibaev/cfgen/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/rzhilkibaev/cfgen/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/rzhilkibaev/cfgen/languages",
    "stargazers_url": "https://api.github.com/repos/rzhilkibaev/cfgen/stargazers",
    "contributors_url": "https://api.github.com/repos/rzhilkibaev/cfgen/contributors",
    "subscribers_url": "https://api.github.com/repos/rzhilkibaev/cfgen/subscribers",
    "subscription_url": "https://api.github.com/repos/rzhilkibaev/cfgen/subscription",
    "commits_url": "https://api.github.com/repos/rzhilkibaev/cfgen/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/rzhilkibaev/cfgen/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/rzhilkibaev/cfgen/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/rzhilkibaev/cfgen/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/rzhilkibaev/cfgen/contents/{+path}",
    "compare_url": "https://api.github.com/repos/rzhilkibaev/cfgen/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/rzhilkibaev/cfgen/merges",
    "archive_url": "https://api.github.com/repos/rzhilkibaev/cfgen/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/rzhilkibaev/cfgen/downloads",
    "issues_url": "https://api.github.com/repos/rzhilkibaev/cfgen/issues{/number}",
    "pulls_url": "https://api.github.com/repos/rzhilkibaev/cfgen/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/rzhilkibaev/cfgen/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/rzhilkibaev/cfgen/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/rzhilkibaev/cfgen/labels{/name}",
    "releases_url": "https://api.github.com/repos/rzhilkibaev/cfgen/releases{/id}",
    "deployments_url": "https://api.github.com/repos/rzhilkibaev/cfgen/deployments",
    "created_at": 1477890271,
    "updated_at": "2016-11-13T03:06:56Z",
    "pushed_at": 1492936912,
    "git_url": "git://github.com/rzhilkibaev/cfgen.git",
    "ssh_url": "git@github.com:rzhilkibaev/cfgen.git",
    "clone_url": "https://github.com/rzhilkibaev/cfgen.git",
    "svn_url": "https://github.com/rzhilkibaev/cfgen",
    "homepage": None,
    "size": 34,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": True,
    "has_projects": True,
    "has_downloads": True,
    "has_wiki": True,
    "has_pages": False,
    "forks_count": 0,
    "mirror_url": None,
    "open_issues_count": 0,
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "master",
    "stargazers": 0,
    "master_branch": "master"
  },
  "pusher": {
    "name": "rzhilkibaev",
    "email": "rzhilkibaev@users.noreply.github.com"
  },
  "sender": {
    "login": "rzhilkibaev",
    "id": 3160853,
    "avatar_url": "https://avatars1.githubusercontent.com/u/3160853?v=3",
    "gravatar_id": "",
    "url": "https://api.github.com/users/rzhilkibaev",
    "html_url": "https://github.com/rzhilkibaev",
    "followers_url": "https://api.github.com/users/rzhilkibaev/followers",
    "following_url": "https://api.github.com/users/rzhilkibaev/following{/other_user}",
    "gists_url": "https://api.github.com/users/rzhilkibaev/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/rzhilkibaev/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/rzhilkibaev/subscriptions",
    "organizations_url": "https://api.github.com/users/rzhilkibaev/orgs",
    "repos_url": "https://api.github.com/users/rzhilkibaev/repos",
    "events_url": "https://api.github.com/users/rzhilkibaev/events{/privacy}",
    "received_events_url": "https://api.github.com/users/rzhilkibaev/received_events",
    "type": "User",
    "site_admin": False
  }
})

apigw_event = {
        u'body': github_webhook_payload_string,
        u'resource': u'/',
        u'requestContext':
        {
            u'resourceId': u'xxxxxxxxxx',
            u'apiId': u'xxxxxxxxxx',
            u'resourcePath': u'/',
            u'httpMethod': u'POST',
            u'requestId': u'xxxxxxxxxxxxxxxxxxx',
            u'accountId': u'xxxxxxxxxxxx',
            u'identity': {
                u'apiKey': u'test-invoke-api-key',
                u'userArn': u'arn:aws:iam::xxxxxxxxxxxx:user/xx',
                u'cognitoAuthenticationType': None,
                u'accessKey': u'XXXXXXXXXXXXXXXXXXXX',
                u'caller': u'XXXXXXXXXXXXXXXXXXXXX',
                u'userAgent': u'Apache-HttpClient/4.5.x (Java/1.8.0_112)',
                u'user': u'XXXXXXXXXXXXXXXXXXXXX',
                u'cognitoIdentityPoolId': None,
                u'cognitoIdentityId': None,
                u'cognitoAuthenticationProvider': None,
                u'sourceIp': u'test-invoke-source-ip',
                u'accountId': u'xxxxxxxxxxxx'
                },
            u'stage': u'test-invoke-stage'
            },
        u'queryStringParameters': None,
        u'httpMethod': u'POST',
        u'pathParameters': None,
        u'headers': None,
        u'stageVariables': None,
        u'path': u'/',
        u'isBase64Encoded': False
        }


@patch("main.publish_event", MagicMock())
def test_build_request_published():
    response = main.handler(apigw_event, None)
    actual_interaction_id = response["headers"]["X-Shmenkins-InteractionId"]
    assert len(actual_interaction_id) == 36
    expected_message = {"interaction_id": ANY, "url": "https://github.com/rzhilkibaev/cfgen"}
    main.publish_event.assert_called_with(expected_message)

