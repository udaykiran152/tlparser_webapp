from datetime import datetime
import streamlit as st

st.title("Graphical User Interface for TL Parser")

if __name__ ==  "__main__" :

  file = st.sidebar.file_uploader(" Upload the TimeLog file here")
  if st.sidebar.button("Generate"):
    line = str(file.read(),"utf-8")

  cnt = 1
  count = 0
  total = 0
  while line:
    if "am" not in line or "pm" not in line :
         count += 1
    else:

      words = line.split(': ')
      words
      start_time = words[-1].split('- ')
      str2 = start_time[-1].strip()
      end_time = str2.split(" ")
      x = start_time[0].strip()
      x = x.split(":")
      y = x[0] + ":" + x[1][:2] + " " + x[1][2:].upper()
      a = end_time[0].strip()
      a = a.split(":")
      b = a[0] + ":" + a[1][:2] + " " + a[1][2:].upper()
      in_time = datetime.strptime(y,"%I:%M %p")
      int_time = datetime.strftime(in_time, "%H:%M")
      int_time = datetime.strptime(int_time,"%H:%M")
      ou_time = datetime.strptime(b,"%I:%M %p")
      out_time = datetime.strftime(ou_time, "%H:%M")
      out_time = datetime.strptime(out_time,"%H:%M")
      diff = (out_time - int_time)
      difference = diff.total_seconds()/60/60
      total += difference
    line = file.readline()
    cnt += 1
st.markdown("### Time spend on this file")
st.write(abs(total))
st.markdown("### Number of lines without timeline")
st.write(count)
