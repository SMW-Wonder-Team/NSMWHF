; Starts at $7E0010, but don't ever point to a random address (always use the label if you decide to use this feature of the framework)
; ~32,000bytes saved by NSMWHF, rest must be manually cleared
; Format like this:
;  #ram(label, bytes)