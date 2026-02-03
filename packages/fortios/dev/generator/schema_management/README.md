# Schema Management

This directory contains all schema-related files and tools for the FortiOS API generator.

## Contents

### Files

- **`download_schemas.py`** - Downloads FortiOS API schemas from FortiGate devices
- **`schema_parser.py`** - Parses JSON schemas into structured metadata
- **`swagger_parser.py`** - Parses Swagger documentation for LOG endpoints

### Directories

- **`swagger/`** - Swagger documentation files for LOG category endpoints

## Usage

### Download Schemas

Download schemas from a FortiGate device:

```bash
python download_schemas.py --host 192.168.1.99 --username admin --version 7.6.5
```

### Schema Location

Downloaded schemas are stored in `/app/dev/classes/fortinet/schema/{version}/` directory structure:
- `schema/7.6.5/cmdb/` - Configuration endpoints
- `schema/7.6.5/monitor/` - Monitoring endpoints  
- `schema/7.6.5/log/` - Log endpoints

## Integration

These modules are imported by `generate.py`:
- `SchemaParser` - Parses schema files for endpoint generation
- `SwaggerParser` - Parses swagger docs for LOG endpoints

See `../README.md` for overall generator documentation.
