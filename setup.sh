if [ ! -d "venv" ]; then
    echo "Creating virtual environment venv ... "
    /usr/bin/python3 -m pip install virtualenv
    /usr/bin/python3 -m virtualenv venv
    echo "Done!"
fi

echo "Activating virtual environment venv ..."
source venv/bin/activate
cd backend
python3 setup.py install 
echo "Done"