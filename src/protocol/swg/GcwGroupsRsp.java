/*******************************************************************************
 * Copyright (c) 2013 <Project SWG>
 * 
 * This File is part of NGECore2.
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * Using NGEngine to work with NGECore2 is making a combined work based on NGEngine. 
 * Therefore all terms and conditions of the GNU Lesser General Public License cover the combination.
 ******************************************************************************/
package protocol.swg;

import java.nio.ByteOrder;
import java.util.Map;

import org.apache.mina.core.buffer.IoBuffer;

import resources.common.Opcodes;
import resources.gcw.CurrentServerGCWZonePercent;

public class GcwGroupsRsp extends SWGMessage {
	
	private Map<String, Map<String, CurrentServerGCWZonePercent>> zoneMap;
	
	public GcwGroupsRsp(Map<String, Map<String, CurrentServerGCWZonePercent>> zoneMap) {
		this.zoneMap = zoneMap;
	}
	
	public void deserialize(IoBuffer data) {
		
	}
	
	public IoBuffer serialize() {
		IoBuffer result = IoBuffer.allocate(9948).order(ByteOrder.LITTLE_ENDIAN);
		
		result.putShort((short) 2);
		result.putInt(Opcodes.GcwGroupsRsp);
		result.putInt(zoneMap.size());
		
		for (String planet : zoneMap.keySet()) {
			result.put(getAsciiString(planet));
			result.putInt(zoneMap.get(planet).size());
			
			for (String zone : zoneMap.get(planet).keySet()) {
				result.put(getAsciiString(zone));
				result.putInt(zoneMap.get(planet).get(zone).getGroup());
			}
		}
		
		return result.flip();
	}
	
}
