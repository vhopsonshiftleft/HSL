#!/usr/bin/python
# Copyright 2020 ShiftLeft, Inc.  All Rights Reserved.
import os
import sys
import argparse
import requests
from urllib.parse import quote as urlquote

##
# Acceptance Criterion
#
# This routine gets the information from an API query against the desired
# project and returns the data in the standard ShiftLeft JSON format.
# That has been deserialized into a dictionary for queries.
def acceptanceCriterion(data) :
    return 0

##
# Main Entry Point
#
def main(args) :

    # Check all of our values and report anything that is not ready.
    # Currently:
    #   org     - for OrgId
    #   app     - for the Application Base Name (mandatory command line)
    #   version - for the Application Version under the Base Name (mandatory command line)
    #   token   - the API token
    org_id = args.org
    if org_id == "" :
        print("\nError -- no ShiftLeft Org Id specified (--org)")
        sys.exit(1)
    else :
        org_id = urlquote(org_id)

    apiToken = args.token
    if apiToken == "" :
        print("\nError -- no ShiftLeft API Token specified (--token)")
        sys.exit(2)

    app = args.app
    if app == "" :
        print("\nError -- no Application name specified (--app)")
        sys.exit(3)
    else :
        app = urlquote(app)

    version = args.version
    if version == "" :
        print("\nError -- no application Version specified (--version)")
        sys.exit(4)
    else :
        version = urlquote(version)

    # Build our URL
    url = "https://www.shiftleft.io/api/v3/public/org/" + org_id
    url += "/app/" + app
    url += "/version/" + args.version 
    url += "/vulnerabilities"

    # set up header authorization
    headers = { "Authorization" : "Bearer " + apiToken,
                "Accept" : "*/*",
                "Content-Type" : "application/json" 
              }

    # set up query payload
    query = { "orderByDirection"  : "VULNERABILITY_ORDER_DIRECTION_DESC"}
    payload = { "query" : query }

    # get session and issue query
    sess = requests.session()
    sess.headers.update(headers)
    resp = sess.post(url, json = payload)
    if resp.status_code != 200 :
        print("Query to ShiftLeft server returned [%d]" % resp.status_code)
        sys.exit(9)

    # return this result
    return acceptanceCriterion(resp.json())


##
# Environment Entry Point
#
description = """
Gather information from the user's ShiftLeft server and
determine if parameters for an analysis were successful.
A subroutine named "acceptanceCriterion" is used that is
easily modifiable to allow the user to create complex or
simple reviews of results from ShiftLeft to determine if
a return value of non-zero, or zero are returned.

Any non-zero return value is considered to be a failure.
"""
parser = argparse.ArgumentParser(description = description)
parser.add_argument("--token", "-t", required=False,
                    default = os.getenv("SHIFTLEFT_API_TOKEN", ""),
                    help="ShiftLeft API token.  Overrides environment.")
parser.add_argument("--org", "-o", required=False,
                    default = os.getenv("SHIFTLEFT_ORG_ID", ""),
                    help = "ShiftLeft Org Id")
parser.add_argument("--version", "-v", required=True,
                    help="Branch or version name of the desired results")
parser.add_argument("--app", "-a", required=True, 
                    help="ShiftLeft application to interrogate")

args = parser.parse_args()
if "__main__" == __name__ :
    main(args)
