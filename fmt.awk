BEGIN {
        print "{ \"body\": \"#[ShiftLeft](https://shiftleft.io) -- Inspect Analysis Findings" ;
        print ;
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
  printf "%s: %s\n", $2, $3 ;
  FS = " ";
  $0 = $0;
}

END {
  print "\" }"
}
