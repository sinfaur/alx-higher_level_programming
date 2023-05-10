#!/bin/bash

# Test function
function run_test() {
    local test_name=$1
    local pyfile=$2
    local expected_output=$3

    export PYFILE="$pyfile"
    output=$(./0-run 2>&1)

    if [ "$output" == "$expected_output" ]; then
        echo "$test_name -> Passed"
    else
        echo "$test_name -> Failed"
        echo "Expected: $expected_output"
        echo "Got: $output"
    fi
}

# Test cases
echo "Test 1 - 20%"
cat > test1.py << EOL
#!/usr/bin/python3
print("Hello, World!")
EOL
run_test "Test 1" "test1" "Hello, World!"

echo "Test 2 - 40%"
cat > test2.py << EOL
#!/usr/bin/python3
print("Python is cool")
EOL
run_test "Test 2" "test2" "Python is cool"

echo "Test 3 - 60%"
cat > test3.py << EOL
#!/usr/bin/python3
print("This is a test with special characters: !@#\$%^&*()")
EOL
run_test "Test 3" "test3" "This is a test with special characters: !@#\$%^&*()"

echo "Test 4 - 80%"
cat > test4.py << EOL
#!/usr/bin/python3
print("This is a test with a newline\ncharacter")
EOL
run_test "Test 4" "test4" "This is a test with a newline
character"

echo "Test 5 - 100%"
cat > test5.py << EOL
#!/usr/bin/python3
print("Multiple\nlines\nof\noutput")
EOL
run_test "Test 5" "test5" "Multiple
lines
of
output"

# Cleanup
rm test1.py test2.py test3.py test4.py test5.py
