BEGIN {
        printf "{ \"body\": \"# <img src=\\\"https://mms.businesswire.com/media/20190212005274/en/671131/23/logo_dark800px.jpg\\\" alt=\\\"ShiftLeft\\\" width=\\\"200\\\"/>\\\n# NG-SAST Analysis Compliance Failure\\n\\n" ;
        RS = "\n";
        FS = " ";
        APPL = "nothing";
}

/\[INFO\] Using app/ {
        APPL=$4;
}

/New matching finding / {
  printf "* [ID %s](https://shiftleft.io/findingDetail/%s/%s) %s", $6, APPL, $6, $7 ;
  FS = ":";
  $0 = $0;
}

/New matching finding/ {
  printf "%s: %s\\n", $2, $3 ;
  FS = " ";
  $0 = $0;
}

END {
  print "\" }"
}
