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
package protocol.swg.objectControllerObjects;

import java.nio.ByteOrder;
import java.util.Vector;

import org.apache.mina.core.buffer.IoBuffer;

import engine.resources.objects.SWGObject;
import protocol.swg.ObjControllerMessage;

public class ShowLootBox extends ObjControllerObject {

	private long playerId;
	private Vector<SWGObject> rewards;
	private SWGObject reward;
	
	public ShowLootBox(long playerId, SWGObject reward) {
		this.playerId = playerId;
		this.reward = reward;
	}
	
	public ShowLootBox(long playerId, Vector<SWGObject> rewards) {
		this.playerId = playerId;
		this.rewards = rewards;
	}
	
	@Override
	public void deserialize(IoBuffer data) {

	}

	@Override
	public IoBuffer serialize() {
		IoBuffer buffer;
		
		if (rewards != null)
			buffer = IoBuffer.allocate(20 + (rewards.size() * 8)).order(ByteOrder.LITTLE_ENDIAN);
		
		else
			buffer = IoBuffer.allocate(28).order(ByteOrder.LITTLE_ENDIAN);
		
		buffer.putInt(ObjControllerMessage.SHOW_LOOT_BOX);
		buffer.putLong(playerId);
		
		buffer.putInt(0); // 1 for a black background on icon, 0 or 2 for transparent (default)
		
		if (rewards == null) {
			buffer.putInt(1);
			buffer.putLong(reward.getObjectId());
		} else {
			buffer.putInt(rewards.size());
			for(SWGObject obj : rewards) {
				buffer.putLong(obj.getObjectID());
			}
		}
		return buffer.flip();
	}

}
