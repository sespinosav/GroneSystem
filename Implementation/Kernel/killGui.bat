taskkill /F /FI "WindowTitle eq groneSystemGUI" /T
FOR /L %%A IN (1,1,%1) DO (
  taskkill /F /FI "WindowTitle eq GroneApp%%A" /T
)
FOR /L %%B IN (1,1,%2) DO (
  taskkill /F /FI "WindowTitle eq GroneLog%%B" /T
)
FOR /L %%C IN (1,1,%3) DO (
  taskkill /F /FI "WindowTitle eq GroneFile%%C" /T
)
exit
