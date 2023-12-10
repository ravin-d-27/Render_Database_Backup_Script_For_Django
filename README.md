
<body>

<h1>Database Backup Script</h1>

<p>This script exports data from a Django model and saves it to a CSV file. It is designed to be used as a backup mechanism for your Django project.</p>

<h2>Requirements</h2>

<ul>
    <li>Python 3.x</li>
    <li>Django</li>
</ul>

<h2>Setup</h2>

<ol>
    <li>Clone the repository:</li>

 <pre><code>git clone https://github.com/ravin-d-27/Render_Database_Backup_Script_For_Django.git</code></pre>

 <li>Install the required dependencies:</li>

<pre><code>pip install -r requirements.txt</code></pre>
</ol>

<h2>Usage</h2>

<ol>
    <li>Open the <code>Backup_Script.py</code> file.</li>

<li>Modify the following variables to match your project:</li>

<ul>
        <li><code>Your Project Name.settings</code>: Replace with the actual path to your Django project's settings module.</li>
        <li><code>yourapp</code>: Replace with the actual app name from your Django project.</li>
        <li><code>yourModel</code>: Replace with the actual model name from your Django project</li>
        <li><code>fieldnames</code>: Replace with the actual field names from your Django model.</li>
    </ul>

 <li>Save the script where manage.py file is located.</li>

<li>Run the script:</li>

<pre><code>python backup_script.py</code></pre>

<p>This will export data from the specified Django model to a CSV file.</p>
</ol>

<h2>Configuration</h2>

<ul>
    <li><code>DJANGO_SETTINGS_MODULE</code>: Set the Django settings module path.</li>
    <li><code>fieldnames</code>: Specify the field names to be exported to the CSV file.</li>
    <li><code>backup_file_path</code>: Define the path for the CSV backup file.</li>
</ul>

<h2>Contributing</h2>

<p>Feel free to contribute by opening issues or submitting pull requests.</p>

<h2>License</h2>

<p>This project is licensed under the GNU GENERAL PUBLIC License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
