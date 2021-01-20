BEGIN {
        printf "{ \"body\": \"# <img src=\\\"https://mms.businesswire.com/media/20190212005274/en/671131/23/logo_dark800px.jpg\\\" alt=\\\"ShiftLeft\\\" width=\\\"200\\\"/><p>NG-SAST Analysis Compliance Failure\\n\\n" ;
        RS = "\n";
        FS = " ";
        APPL = "nothing";
}

/^Using application/ {
        APPL=$3;
}

/New matching finding / {
  printf "* [ID %s](https://shiftleft.io/findingDetail/%s/%s) %s", $5, APPL, $5, $6 ;
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
