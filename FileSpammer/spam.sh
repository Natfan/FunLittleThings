i=0

for (( ; ; ))
do
	let "i++"
	touch $i.spam
	echo "+1 spammed files, now at $1 files."
done
