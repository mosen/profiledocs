iBooks
======

Disabling the Book Store
------------------------

To disable the book store you need two payload domains, :ref:`com.apple.iTunes` and
:ref:`com.apple.iBooksX`.

For the iTunes domain, you will need a payload which includes the **disableMusicStore** key, example::

         <dict>
            <key>PayloadType</key>
            <string>com.apple.iTunes</string>
            <key>PayloadIdentifier</key>
            <string>com.github.mosen.itunes.ibooks.example</string>
            <key>PayloadUUID</key>
            <string>AA84C49C-C8FE-41C7-9CDA-FD1F888005FA</string>
            <key>disableMusicStore</key>
            <true/>
        </dict>

For the iBooksX domain, you need to include the **BKDisableBookStorePreferenceKey** key, example::

        <dict>
            <key>PayloadType</key>
            <string>com.apple.iBooksX</string>
            <key>PayloadIdentifier</key>
            <string>com.github.mosen.ibooks.example</string>
            <key>PayloadUUID</key>
            <string>9D84C49C-C8FE-41C7-9CDA-FD3F888005FA</string>
            <key>BKDisableBookStorePreferenceKey</key>
            <true/>
        </dict>


With both of these enabled, the iBooks store will be disabled.

.. note:: The status of the iBooks store is determined by the BookKit private framework.
