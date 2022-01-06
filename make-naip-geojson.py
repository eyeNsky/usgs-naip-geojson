"""Modules to work with USGS NAIP data."""
import os


USE_DOCKER = True


def docker_it(cmd):
    """Convert command to run in docker."""
    cmd = 'docker run -it amazon/aws-cli ' + cmd[4:]
    return cmd


# Example commands
def ls_naip():
    """List the available NAIP data."""
    cmd = 'aws s3 ls  --no-sign-request s3://prd-tnm/StagedProducts/NAIP/'
    if USE_DOCKER:
        cmd = docker_it(cmd)
    os.system(cmd)


def download_naip_index():
    """Download the NAIP index. The index used to generate this geojson was from ~2015."""
    cmd = 'aws s3 cp  --no-sign-request s3://prd-tnm/StagedProducts/NAIP/footprint/naip_src_footprint.zip .'
    if USE_DOCKER:
        cmd = docker_it(cmd)
    os.system(cmd)    

#ls_naip()
download_naip_index()
