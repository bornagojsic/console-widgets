#!/usr/bin/env bash

jumpto () {
    label=$1
    cmd=$(sed -n "/$label:/{:a;n;p;ba};" $0 | grep -v ':$')
    eval "$cmd"
    exit
}

noexpected () {
	echo "The file with the expected result ($1.txt) doesn't exist!"
	jumpto end
}

alltests () {
	for f in `ls tests/`
	do
		if [[ "$f" != "${f%.py}" ]]
		then
			bash $0 $f
		fi
	done

	echo ======== Overall results ========
	cat  tests/tests.results
	echo =================================

	rm tests/tests.results
	jumpto end
}

onetest () {
	test=${1%.py}
	echo $test

	if [[ ! -f tests/expected/$test.txt ]]
	then
		noexpected $test
	fi

	if [[ ! -d tests/results ]]
	then
		mkdir tests/results 
	fi

	### Testing only one example

	echo
	echo Testing $test.py
	echo =========== Expected ============
	cat  tests/expected/$test.txt
	echo ============ Result =============
	STARTTIME=$(date +%s%3N)
	python tests/$test.py > tests/results/$test.txt 2> tests/results/$test.stderr
	ENDTIME=$(date +%s%3N)
	cat  tests/results/$test.txt
	cat  tests/results/$test.stderr
	echo =================================
	totalsecs=$(expr $ENDTIME - $STARTTIME)
	echo
 	echo "Total time: $totalsecs ms"
	echo
 	if cmp --silent -- "tests/expected/$test.txt" "tests/results/$test.txt"
 	then
 		echo "Test $test passed!"
 		echo "Test $test passed!" >> tests/tests.results
 	else
 		echo "Test $test FAILED!"
 		echo "Test $test FAILED!" >> tests/tests.results
 	fi
 	echo
 	jumpto end
}

if [[ ! -f tests/tests.results ]]
then
    touch tests/tests.results
fi

if [[ -n "$1" ]]
then
	onetest $1
else
	alltests
fi

set +v end
echo