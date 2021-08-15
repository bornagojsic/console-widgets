#!/usr/bin/env bash


jumpto () {
    label=$1
    cmd=$(sed -n "/$label:/{:a;n;p;ba};" $0 | grep -v ':$')
    eval "$cmd"
    exit
}


notest () {
	echo "The test file ($1.py) doesn't exist!"
	jumpto end
}


noexpected () {
	echo "The file with the expected result ($1.txt) doesn't exist!"
	jumpto end
}


alltests () {
	if [[ $1 == true ]]
	then
		flag="-c"
	else
		flag=""
	fi

	touch tests/tests.results
	
	for f in `ls tests/`
	do
		if [[ "$f" != "${f%.py}" ]]
		then
			bash $0 $flag $f
		fi
	done

	echo ======== Overall results ========
	cat  tests/tests.results
	echo =================================
	echo

	rm tests/tests.results
	jumpto end
}


passed () {
	if [[ $1 == false ]]
	then
		echo "Test $test $(tput setaf 2)passed$(tput setaf 7)!"
 	fi
 	echo "Test $test $(tput setaf 2)passed$(tput setaf 7)!" >> tests/tests.results
}


failed () {
	if [[ $1 == false ]]
	then
		echo "Test $test $(tput setaf 1)FAILED$(tput setaf 7)!"
	fi
	echo "Test $test $(tput setaf 1)FAILED$(tput setaf 7)!" >> tests/tests.results
}


onetest () {
	test=${1%.py}
	compact=$2

	if [[ ! -f tests/$test.py ]]
	then
		notest $test
	fi

	if [[ ! -f tests/expected/$test.txt ]]
	then
		noexpected $test
	fi

	if [[ ! -d tests/results ]]
	then
		mkdir tests/results 
	fi

	### Testing only one example
	
	if [[ $compact == false ]]
	then
		echo
		echo Testing $test.py
		echo =========== Expected ============
		cat  tests/expected/$test.txt
		echo ============ Result =============
	fi
	
	
	if [[ -f tests/input/$test.in ]]
	then
		STARTTIME=$(date +%s%3N)
		python tests/$test.py < tests/input/$test.in > tests/results/$test.txt 2> tests/results/$test.stderr
		ENDTIME=$(date +%s%3N)
	else
		STARTTIME=$(date +%s%3N)
		python tests/$test.py > tests/results/$test.txt 2> tests/results/$test.stderr
		ENDTIME=$(date +%s%3N)
	fi
	
	
	if [[ $1 == false ]]
	then
		cat  tests/results/$test.txt
		cat  tests/results/$test.stderr
		echo =================================
		totalsecs=$(expr $ENDTIME - $STARTTIME)
		echo
	 	echo "Total time: $totalsecs ms"
		echo
 	fi
 	
 	if cmp --silent -- "tests/expected/$test.txt" "tests/results/$test.txt"
 	then
 		passed $compact
 	else
 		failed $compact
 	fi
 	echo
 	jumpto end
}


compacttest () {
	compact=true
	if [[ -n "$1" ]]
	then
		onetest $1 $compact
	else
		alltests $compact
	fi
}


regulartest () {
	if [[ -n "$1" ]]
	then
		onetest $1 false
	else
		alltests false
	fi
}


if [[ $1 == '-c' ]]
then
	compacttest $2
else
	regulartest $1
fi

set +v end
echo