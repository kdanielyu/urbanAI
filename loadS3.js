function listFiles() {
    AWS.config.update({
        region: '',
        accessKeyId: '',
        secretAccessKey: ''
    });

    var s3 = new AWS.S3();
    //var s3Bucket = new aws.S3( { params: {Bucket: 'urbanai'} } );

    var params = { Bucket: '', Key: 'test.txt' };

    s3.getObject(params, function(err, data){
        if (err) console.log(err, err.stack); // an error occurred
        else     console.log(data); 
    });
}